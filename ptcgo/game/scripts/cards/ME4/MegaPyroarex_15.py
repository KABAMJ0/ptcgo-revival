from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks

card = PokemonCardDef(
    guid="51a83341-7607-5e02-a526-ae40f0cc26f3",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaPyroarex.Name",
    display_name="Mega Pyroar ex",
    searchable_by=["Mega Pyroar ex", "Stage 1", "MEGA", "ex", "MegaPyroarex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=15,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Attack(
            title="Ferocious Bellow",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 50 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=reduce_defender_attacks(50),
        ),
        Attack(
            title="Fiery Big Bang",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=290,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)