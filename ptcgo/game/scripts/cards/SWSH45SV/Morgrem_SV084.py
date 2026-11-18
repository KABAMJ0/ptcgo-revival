from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="1a104240-fd29-5855-9112-4a1a0e3c9df4",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    display_name="Morgrem",
    searchable_by=["Morgrem", "Stage 1", "Morgrem"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="False Surrender",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)