from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.card_effects.attacks_common import mill_attack


card = PokemonCardDef(
    guid="796cb41b-6e2c-51c8-9289-408e53329097",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsireex.Name",
    display_name="Paldean Clodsire ex",
    searchable_by=["Paldean Clodsire ex", "Stage 1", "ex", "PaldeanClodsireex"],
    subtypes=["Stage 1", "ex"],
    collector_number=94,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During your opponent's next turn, that Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=mill_attack(1, opponent=True),
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=lock_self_attack(),
        ),
    ],
)