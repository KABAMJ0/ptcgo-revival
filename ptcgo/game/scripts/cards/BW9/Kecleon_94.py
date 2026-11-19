from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, def_for
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.legal_actions import attack_cost_satisfied
from ptcgo.game.session.passives import Passive


def _playmat(entity):
    node = entity
    while getattr(node, "parent", None) is not None:
        node = node.parent
    return node


def _opposing_active(pokemon):
    """The other side's Active Pokemon, found through the playmat tree
    (modify_pokemon_types is handed no board)."""
    for player in _playmat(pokemon).children:
        if getattr(player, "owning_player_id", None) == pokemon.owning_player_id:
            continue
        for area in player.children:
            if area.get_attribute(AttrID.NAME) == "activePokemonArea" and area.children:
                return area.children[0]
    return None


async def imittack(ctx):
    """Use one of the Defending Pokemon's attacks, but only one this Pokemon
    could pay for."""
    defender = ctx.defender
    if defender is None:
        return
    energies = ctx.attached_energies(ctx.attacker)
    candidates = [
        (defender, entry)
        for entry in getattr(def_for(defender.archetype_id), "abilities", None) or []
        if isinstance(entry, Attack)
        and attack_cost_satisfied(entry.cost or {}, energies, ctx.board)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(
        candidates, "Choose an attack to use as Imittack")
    if picked is None:
        return
    await ctx.use_attack(picked[1], source=defender)


class ColorChangePassive(Passive):
    """While this Pokemon is Active its type is the opposing Active's type."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier or not is_in_active_spot(carrier):
            return types
        opponent = _opposing_active(carrier)
        if opponent is None:
            return types
        return list(opponent.get_attribute(AttrID.POKEMON_TYPES) or []) or types

card = PokemonCardDef(
    guid="525953ca-598a-5dfb-abee-966acf3dd4ea",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic", "Kecleon"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Color Change",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, this Pok\u00e9mon is the same type as the your opponent's Active Pok\u00e9mon.",
            passive=ColorChangePassive(),
        ),
        Attack(
            title="Imittack",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. If this Pok\u00e9mon has the necessary Energy to use that attack, use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=imittack,
        ),
    ],
)