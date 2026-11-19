from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.passives_common import Passive, is_in_active_spot


class _Wall(Passive):
    """-10 to every opposing attack against the owner while Unown W is Active."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        holder = carrier_pokemon(carrier)
        if holder is None or not is_in_active_spot(holder):
            return
        if calc.target.owning_player_id != carrier.owning_player_id:
            return
        calc.amount -= 10

card = PokemonCardDef(
    guid="e3fc7bef-603d-5b56-9008-e2277115ca9c",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownW.Name",
    display_name="Unown [W]",
    searchable_by=["Unown [W]", "Basic", "UnownW"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="WALL",
            game_text="As long as Unown W is your Active Pok\u00e9mon, any damage done to your Pok\u00e9mon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            passive=_Wall(),
        ),
        Attack(
            title="Hidden Power",
            game_text="Draw a card.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=draw_attack(1),
        ),
    ],
)