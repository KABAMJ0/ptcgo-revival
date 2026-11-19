from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c4d841d-f7f5-5042-88cd-05a3f55af9d9",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic", "Ponyta"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Ability(
            title="Star Barrier",
            game_text="As long as Ponyta has any Energy attached to it, Ponyta has no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Blue Fire",
            game_text="Discard all Fire Energy attached to Ponyta.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.FIRE),
        ),
    ],
)