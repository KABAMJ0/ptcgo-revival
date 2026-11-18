from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37266f87-9e93-5b5d-a08f-d56e6669df72",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BeedrillG.Name",
    display_name="Beedrill G",
    searchable_by=["Beedrill G", "Basic", "SP", "BeedrillG"],
    subtypes=["Basic", "SP"],
    collector_number=53,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=15,
    abilities=[
        Attack(
            title="Raid",
            game_text="If you played Beedrill G from your hand during this turn, this attack's base damage is 40 instead of 10.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
    ],
)