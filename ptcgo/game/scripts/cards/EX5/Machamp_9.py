from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_bonus, ignore_modifier_attack

card = PokemonCardDef(
    guid="248701f1-3c37-50e0-bb61-fc0c043b0cc3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Overzealous",
            game_text="If your opponent has any Pok\u00e9mon-ex in play, each of Machamp's attacks do 30 more damage to the Defending Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Brick Smash",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True),
        ),
        Attack(
            title="Cross Chop",
            game_text="Flip a coin. If heads, this attack does 60 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)