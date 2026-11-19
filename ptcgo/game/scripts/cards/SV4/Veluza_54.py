from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84d9ad10-1bbf-56c9-b7bc-28231a65f7ae",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name",
    display_name="Veluza",
    searchable_by=["Veluza", "Basic", "Veluza"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=976,
    abilities=[
        Ability(
            title="Fillet Memento",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, move up to 2 Water Energy cards from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            effect=damage_per(count_energy("self", "water"), 20),
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)