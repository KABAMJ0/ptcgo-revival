from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="7d75c670-c187-5dd4-aca3-4afbcdf25991",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaGX.Name",
    display_name="Dialga-GX",
    searchable_by=["Dialga-GX", "Basic", "GX", "DialgaGX"],
    subtypes=["Basic", "GX"],
    collector_number=164,
    set_code="SM5",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=483,
    abilities=[
        Attack(
            title="Overclock",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.METAL: 1},
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
        Attack(
            title="Timeless-GX",
            game_text="Take another turn after this one. (Skip the between-turns step.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)