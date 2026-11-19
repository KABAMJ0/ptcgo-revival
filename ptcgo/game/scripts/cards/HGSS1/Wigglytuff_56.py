from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="45e4107e-e06b-5eac-8774-7e6add9fab5e",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
        Attack(
            title="Expand",
            game_text="During your opponent's next turn, any damage done to Wigglytuff by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)