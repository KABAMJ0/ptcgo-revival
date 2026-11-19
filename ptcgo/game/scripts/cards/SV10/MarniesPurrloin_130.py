from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.trainers import is_pokemon_ex
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4de86b0-356c-5a50-970c-a74e0291ad9f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesPurrloin.Name",
    display_name="Marnie's Purrloin",
    searchable_by=["Marnie's Purrloin", "Basic", "MarniesPurrloin"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=509,
    abilities=[
        Attack(
            title="Pointy Nails",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 40 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_pokemon_ex(ctx.defender), 40),
        ),
    ],
)