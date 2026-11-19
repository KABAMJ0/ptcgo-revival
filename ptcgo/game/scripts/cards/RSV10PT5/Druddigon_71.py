from ptcgo.game.card_effects.attacks_common import flip_bonus, ignore_modifier_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70b91c70-ba9c-5f8a-84da-f1fc4e9e9c61",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic", "Druddigon"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=621,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=flip_bonus(60),
        ),
    ],
)