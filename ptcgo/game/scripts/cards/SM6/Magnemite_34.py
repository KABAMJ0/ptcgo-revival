from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="3e83f226-b7a9-5da7-9c01-c759cf101cd0",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=81,
    abilities=[
        Attack(
            title="Searching Magnet",
            game_text="Search your deck for up to 3 Lightning Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(basic_energy_of("lightning"), count=3, minimum=0, reveal=True),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)