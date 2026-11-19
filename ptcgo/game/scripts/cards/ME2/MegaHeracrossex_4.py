from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_attack

card = PokemonCardDef(
    guid="f8c71aa2-458a-5b14-8ba2-987f995f4368",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaHeracrossex.Name",
    display_name="Mega Heracross ex",
    searchable_by=["Mega Heracross ex", "Basic", "MEGA", "ex", "MegaHeracrossex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=4,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Juggernaut Horn",
            game_text="If this Pok\u00e9mon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Mountain Ramming",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.GRASS: 3},
            damage=170,
            effect=mill_attack(count=2),
        ),
    ],
)