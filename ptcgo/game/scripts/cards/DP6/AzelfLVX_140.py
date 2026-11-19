from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, place_counters
from ptcgo.game.card_effects.passives_common import no_weakness_passive, team_of_types


card = PokemonCardDef(
    guid="88a6d6d8-7d92-5426-90e5-7c254944257d",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AzelfLVX.Name",
    display_name="Azelf LV.X",
    searchable_by=["Azelf LV.X", "Level-Up", "AzelfLVX"],
    subtypes=["Level-Up"],
    collector_number=140,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name",
    family_id=482,
    abilities=[
        Ability(
            title="Psychic Aura",
            game_text="Each of your Psychic Pok\u00e9mon has no Weakness.",
            passive=no_weakness_passive(protects=team_of_types(PokemonTypes.PSYCHIC)),
        ),
        Attack(
            title="Deep Balance",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Put 1 damage counter on that Pok\u00e9mon for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(count_energy("opponent", cards=True), target="choose_any_opponent"),
        ),
    ],
)