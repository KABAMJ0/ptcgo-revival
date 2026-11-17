from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cec6e6ad-9b6c-52c7-846e-83912b81e8fb",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Attack(
            title="Cleansing Ring",
            game_text="You may discard 2 cards from your hand. If you do, remove 4 damage counters from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Scale Blow",
            game_text="Does 90 damage minus 10 damage for each card in your hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)