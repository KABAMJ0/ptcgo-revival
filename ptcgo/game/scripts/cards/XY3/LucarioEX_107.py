from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="feb55d40-93f0-5e2c-89d4-9b39f88c0d90",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioEX.Name",
    display_name="Lucario-EX",
    searchable_by=["Lucario-EX", "Basic", "EX", "LucarioEX"],
    subtypes=["Basic", "EX"],
    collector_number=107,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=448,
    abilities=[
        Attack(
            title="Missile Jab",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
        Attack(
            title="Corkscrew Smash",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Somersault Kick",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
        ),
    ],
)