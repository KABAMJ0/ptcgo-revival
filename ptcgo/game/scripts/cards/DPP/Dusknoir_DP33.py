from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e3853aa8-8c23-593e-80b9-464b4735d674",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=477,
    abilities=[
        Ability(
            title="Dark Hide",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, look at your opponent's hand, choose a Pok\u00e9mon you find there, and put it on the bottom of his or her deck. This power can't be used if Dusknoir is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Reaper Pulse",
            game_text="Move up to 2 damage counters from Dusknoir to 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)