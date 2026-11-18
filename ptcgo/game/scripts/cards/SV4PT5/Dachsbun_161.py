from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="828622a8-cc70-544b-865b-75f7dd8c11c8",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dachsbun.Name",
    display_name="Dachsbun",
    searchable_by=["Dachsbun", "Stage 1", "Dachsbun"],
    subtypes=["Stage 1"],
    collector_number=161,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
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