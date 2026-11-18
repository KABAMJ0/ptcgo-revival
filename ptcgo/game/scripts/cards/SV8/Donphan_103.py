from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="7b765f7c-8cfb-51df-8bad-4ed4dfac1590",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1", "Donphan"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="Knock Flat",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
        Attack(
            title="Guarded Rolling",
            game_text="Discard 2 Energy from this Pok\u00e9mon. During your opponent's next turn, this Pok\u00e9mon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)