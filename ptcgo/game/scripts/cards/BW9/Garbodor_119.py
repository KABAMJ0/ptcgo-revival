from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import has_tool
from ptcgo.game.session.passives import Passive


class GarbotoxinPassive(Passive):
    """With a Pokemon Tool attached, every other Pokemon in play has no
    Abilities."""

    def blocks_abilities(self, pokemon, carrier):
        return pokemon is not carrier and has_tool(carrier)

card = PokemonCardDef(
    guid="e0cdf7cc-8434-54b4-bf0c-de03926e24d3",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="BW9",
    rarity=Rarities.RareSecret,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=569,
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