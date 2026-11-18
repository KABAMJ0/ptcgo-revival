from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="752916b0-9932-5d54-baaf-c5c2fe16bae6",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    display_name="Duosion",
    searchable_by=["Duosion", "Stage 1", "Duosion"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    family_id=577,
    abilities=[
        Attack(
            title="Cellular Evolution",
            game_text="Search your deck for a card that evolves from 1 of your Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spray Fluid",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)