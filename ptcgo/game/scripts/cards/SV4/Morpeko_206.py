from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import no_energy_free_retreat_passive

card = PokemonCardDef(
    guid="678480d9-ea8b-5fda-9230-0d64a9500bf7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic", "Morpeko"],
    subtypes=["Basic"],
    collector_number=206,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Ability(
            title="In a Hungry Hurry",
            game_text="If this Pok\u00e9mon has no Energy attached, it has no Retreat Cost.",
            passive=no_energy_free_retreat_passive(),
        ),
        Attack(
            title="Energizer Wheel",
            game_text="Move 2 Darkness Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)