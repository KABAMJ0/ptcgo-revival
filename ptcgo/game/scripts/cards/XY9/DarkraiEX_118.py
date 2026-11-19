from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
card = PokemonCardDef(
    guid="cdf89d4e-c282-58b8-9b1f-e971d3dcf595",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiEX.Name",
    display_name="Darkrai-EX",
    searchable_by=["Darkrai-EX", "Basic", "EX", "DarkraiEX"],
    subtypes=["Basic", "EX"],
    collector_number=118,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=491,
    abilities=[
        Attack(
            title="Dark Pulse",
            game_text="This attack does 20 more damage for each Darkness Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("mine", energy_type=PokemonTypes.DARKNESS), 20, base=20),
        ),
        Attack(
            title="Dark Head",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)