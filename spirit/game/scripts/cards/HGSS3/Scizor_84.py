from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="941d228a-4942-578f-846a-1688d32555dd",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Prime", "Scizor"],
    subtypes=["Stage 1", "Prime"],
    collector_number=84,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Ability(
            title="Red Armor",
            game_text="Prevent all damage done to Scizor by attacks from your opponent's Pok\u00e9mon that have any Special Energy cards attached to them.",
            effect=unimplemented,
        ),
        Attack(
            title="Metal Scissors",
            game_text="Does 30 damage plus 20 more damage for each Metal Energy attached to Scizor.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)