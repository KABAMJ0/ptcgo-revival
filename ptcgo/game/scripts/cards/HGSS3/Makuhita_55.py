from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="7808dd74-c911-5fa4-a3be-e7aa02561547",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    display_name="Makuhita",
    searchable_by=["Makuhita", "Basic", "Makuhita"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=296,
    abilities=[
        Attack(
            title="Slap Down",
            game_text="Flip 2 coins. This attack does 20 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins=2, base=20, bonus_per_heads=10),
        ),
        Attack(
            title="Slap Push",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)