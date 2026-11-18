from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="26cc90a3-d20d-5492-afea-6c994cfa06e2",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLatiasex.Name",
    display_name="Mega Latias ex",
    searchable_by=["Mega Latias ex", "Basic", "MEGA", "ex", "MegaLatiasex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=181,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=380,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Illusory Impulse",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=300,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)