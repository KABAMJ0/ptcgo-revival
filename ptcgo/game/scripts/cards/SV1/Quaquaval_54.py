from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8e535226-93e4-5e35-91ae-ab6274016ca5",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaquaval.Name",
    display_name="Quaquaval",
    searchable_by=["Quaquaval", "Stage 2", "Quaquaval"],
    subtypes=["Stage 2"],
    collector_number=54,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    family_id=912,
    abilities=[
        Ability(
            title="Energy Carnival",
            game_text="Once during your turn, you may attach a Basic Energy card from your hand to 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Kick",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)