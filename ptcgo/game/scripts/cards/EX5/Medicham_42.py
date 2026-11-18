from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="78130d9f-7f56-54cb-b5c4-6d872a13eb1a",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Steady Punch",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(30)),
        ),
        Attack(
            title="Power Heal",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Medicham. After doing damage, remove 1 damage counter from Medicham.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)