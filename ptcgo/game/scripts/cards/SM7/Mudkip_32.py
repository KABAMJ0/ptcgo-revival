from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="4e6ce8a5-1bef-5d1b-8c44-626c575c3eb3",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    display_name="Mudkip",
    searchable_by=["Mudkip", "Basic", "Mudkip"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=258,
    abilities=[
        Attack(
            title="Water Reserve",
            game_text="Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(basic_energy_of("water"), count=3, minimum=0, reveal=True),
        ),
    ],
)