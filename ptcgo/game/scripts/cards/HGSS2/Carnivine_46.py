from ptcgo.game.card_effects.support_common import search_to_hand, is_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70e102e6-b0b4-50f2-937f-f9cffa75dac7",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=455,
    abilities=[
        Attack(
            title="Drawup Power",
            game_text="Search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(predicate=is_energy, count=1, minimum=1),
        ),
        Attack(
            title="Spit Up",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)