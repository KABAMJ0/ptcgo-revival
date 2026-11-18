from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b0a62d74-81b4-5540-8085-5658a16be821",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    display_name="Floette",
    searchable_by=["Floette", "Stage 1", "Floette"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    family_id=669,
    abilities=[
        Attack(
            title="Swirling Petals",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. If you do, switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            effect=unimplemented,
        ),
    ],
)