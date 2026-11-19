from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.models.board import PlayerEntity, PokemonEntity
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.session.passives import Passive


def _opposing_active(carrier):
    """The opponent's Active Pokemon, read off the playmat from the carrier."""
    owner = carrier.parent.parent if carrier.parent is not None else None
    playmat = owner.parent if owner is not None else None
    for sibling in getattr(playmat, "children", None) or ():
        if sibling is owner or not isinstance(sibling, PlayerEntity):
            continue
        for area in sibling.children:
            if area.get_attribute(AttrID.NAME) != "activePokemonArea":
                continue
            for card in area.children:
                if isinstance(card, PokemonEntity):
                    return card
    return None


class UnobservantPassive(Passive):
    """"If your opponent's Active Pokemon is a Basic Pokemon, this Pokemon
    can't attack." -- a self-only attack ban, not a board-wide one."""

    def blocks_attack(self, pokemon, carrier):
        if pokemon is not carrier:
            return False
        active = _opposing_active(carrier)
        return active is not None and is_basic_pokemon(active)


card = PokemonCardDef(
    guid="2fd74bde-49cd-5446-8e28-7e9622c4f0be",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Unobservant",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, this Pok\u00e9mon can't attack.",
            passive=UnobservantPassive(),
        ),
        Attack(
            title="Crushing Blow",
            game_text="Discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)
