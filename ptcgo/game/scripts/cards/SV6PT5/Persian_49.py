from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="47ce89d7-8e48-5f4b-8685-31953423d1a2",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=50),
        ),
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)