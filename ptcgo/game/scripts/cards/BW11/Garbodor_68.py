from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import has_tool
from ptcgo.game.session.passives import Passive, carrier_pokemon


class GarbotoxinPassive(Passive):
    """While this Pokemon has a Pokemon Tool attached, every Pokemon in play has
    no Abilities. The carrier keeps its own, which is the printed "except for
    Garbotoxin" clause."""

    def blocks_abilities(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or pokemon is holder:
            return False
        return has_tool(holder)


card = PokemonCardDef(
    guid="50b5a4d3-a0a7-55a1-bb43-afae39609b6b",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Ability(
            title="Garbotoxin",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, each Pok\u00e9mon in play, in each player's hand, and in each player's discard pile has no Abilities (except for Garbotoxin).",
            passive=GarbotoxinPassive(),
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)