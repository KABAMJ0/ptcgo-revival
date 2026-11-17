from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5032b8fe-98bb-56ca-a2f3-93ca4cfd34dc",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=303,
    abilities=[
        Ability(
            title="Special Eater",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)