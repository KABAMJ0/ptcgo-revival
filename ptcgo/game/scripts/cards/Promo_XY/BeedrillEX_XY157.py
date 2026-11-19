from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ebb8aca8-bdbf-52a7-96df-419be16e0c28",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BeedrillEX.Name",
    display_name="Beedrill-EX",
    searchable_by=["Beedrill-EX", "Basic", "EX", "BeedrillEX"],
    subtypes=["Basic", "EX"],
    collector_number=157,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=15,
    abilities=[
        Attack(
            title="Double Scrapper",
            game_text="Discard up to 2 Pok\u00e9mon Tool cards attached to your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=40),
        ),
    ],
)