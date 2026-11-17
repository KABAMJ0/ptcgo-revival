from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4426665-5b75-5876-9eb0-56613f58a8a2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    display_name="Dottler",
    searchable_by=["Dottler", "Stage 1", "Dottler"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    family_id=824,
    abilities=[
        Attack(
            title="Protect",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)