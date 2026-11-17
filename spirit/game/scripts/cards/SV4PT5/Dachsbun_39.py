from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4df5a030-f04c-5512-b8d9-4f47fcfac327",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dachsbun.Name",
    display_name="Dachsbun",
    searchable_by=["Dachsbun", "Stage 1", "Dachsbun"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    family_id=926,
    abilities=[
        Ability(
            title="Well-Baked Body",
            game_text="This Pok\u00e9mon can't be Burned. Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Fire Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)