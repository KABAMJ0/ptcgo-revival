from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="dc49b927-f01f-5a24-966f-24b37ca13c1f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensSkarmory.Name",
    display_name="Steven's Skarmory",
    searchable_by=["Steven's Skarmory", "Basic", "StevensSkarmory"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Sonic Double",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(50, pool="any", count=2, apply_modifiers=False),
        ),
    ],
)