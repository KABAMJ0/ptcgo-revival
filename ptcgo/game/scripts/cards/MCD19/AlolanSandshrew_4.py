from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="5508ef73-ed0f-58b2-a14e-bafa7764c599",
    key="MCD19",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    display_name="Alolan Sandshrew",
    searchable_by=["Alolan Sandshrew", "Basic", "AlolanSandshrew"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="MCD19",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=27,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={},
            damage=10,
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)