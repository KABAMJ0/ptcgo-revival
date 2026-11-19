from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
card = PokemonCardDef(
    guid="5c232300-654b-53f9-9d27-9b5166efcf49",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopaex.Name",
    display_name="Hoopa ex",
    searchable_by=["Hoopa ex", "Basic", "Tera", "ex", "Hoopaex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=98,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Attack(
            title="Energy Crush",
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_energy("opponent"), 50),
        ),
        Attack(
            title="Bandit's Fist",
            game_text="During your next turn, this Pok\u00e9mon can't use Bandit's Fist.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)