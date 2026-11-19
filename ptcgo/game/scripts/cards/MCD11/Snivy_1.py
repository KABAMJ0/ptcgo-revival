from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9ab274ab-c35f-5689-a192-52d1327c1b4f",
    key="MCD11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    display_name="Snivy",
    searchable_by=["Snivy", "Basic", "Snivy"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="MCD11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=495,
    abilities=[
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)