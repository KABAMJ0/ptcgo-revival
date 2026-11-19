from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack, snipe_attack

card = PokemonCardDef(
    guid="77809d35-dd4e-58b8-8f2d-6f3d231ff067",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BuzzwoleGX.Name",
    display_name="Buzzwole-GX",
    searchable_by=["Buzzwole-GX", "Basic", "GX", "Ultra Beast", "BuzzwoleGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=57,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=794,
    abilities=[
        Attack(
            title="Jet Punch",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=snipe_attack(30, pool="bench", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Knuckle Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=160,
            effect=lock_self_attack(),
        ),
        Attack(
            title="Absorption-GX",
            game_text="This attack does 40 damage for each of your remaining Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)