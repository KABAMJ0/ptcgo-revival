from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="095b43c1-7b66-5676-9bdc-ef0b5795a229",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dachsbun.Name",
    display_name="Dachsbun",
    searchable_by=["Dachsbun", "Stage 1", "Dachsbun"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="SV1",
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