from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="05e0fbb9-ec28-52c3-8111-7b76d6975539",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaquaval.Name",
    display_name="Quaquaval",
    searchable_by=["Quaquaval", "Stage 2", "Quaquaval"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SVP",
    rarity=Rarities.RarePromo,
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