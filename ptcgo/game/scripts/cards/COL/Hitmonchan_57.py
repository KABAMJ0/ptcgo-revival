from ptcgo.game.card_effects.passives_common import flip_protection
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="82e3e7cd-3b0d-5b1c-ac2f-b7a6b98278ad",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name",
    display_name="Hitmonchan",
    searchable_by=["Hitmonchan", "Basic", "Hitmonchan"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="COL",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Detect",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to Hitmonchan during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(effects_too=True),
        ),
        Attack(
            title="Sky Uppercut",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)