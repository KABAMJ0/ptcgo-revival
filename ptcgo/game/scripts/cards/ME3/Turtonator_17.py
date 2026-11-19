from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="677c0ef6-05b9-5238-a1af-a608f0d978ca",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Ability(
            title="Shell Spikes",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), discard an Energy from the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Heat Breath",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(80),
        ),
    ],
)