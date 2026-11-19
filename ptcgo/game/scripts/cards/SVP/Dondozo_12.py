from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="b573d352-feff-580a-a42c-a95b6df21bfc",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dondozo.Name",
    display_name="Dondozo",
    searchable_by=["Dondozo", "Basic", "Dondozo"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=977,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Dangerous Wave",
            game_text="Flip 2 coins. If both of them are heads, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=flip_damage(coins=2, require_all=True, base=100, bonus=100),
        ),
    ],
)