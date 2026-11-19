from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="056dffcc-3689-5f3e-b5ae-89fe31b9aed2",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaGX.Name",
    display_name="Dialga-GX",
    searchable_by=["Dialga-GX", "Basic", "GX", "DialgaGX"],
    subtypes=["Basic", "GX"],
    collector_number=138,
    set_code="SM6",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
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