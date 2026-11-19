from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack, snipe_attack

card = PokemonCardDef(
    guid="d091d396-b96f-57eb-8aee-7f24fd0fd599",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Feint Attack",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance, or by any effects on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=snipe_attack(50, pool="any"),
        ),
        Attack(
            title="Pitch-Black Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=lock_self_attack(),
        ),
    ],
)