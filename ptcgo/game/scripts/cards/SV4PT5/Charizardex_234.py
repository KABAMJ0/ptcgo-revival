from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from ptcgo.game.card_effects.attacks_common import count_prizes_taken, damage_per
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="34f4c8f6-32da-5186-9146-8e29ca39e908",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizardex.Name",
    display_name="Charizard ex",
    searchable_by=["Charizard ex", "Stage 2", "Tera", "ex", "Charizardex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=234,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Infernal Reign",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may search your deck for up to 3 Basic Fire Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=search_attach_energy(predicate=basic_energy_of("Fire"), count=3, distribute=True),
        ),
        Attack(
            title="Burning Darkness",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.FIRE: 2},
            damage=180,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("opponent"), per=30, base=180),
        ),
    ],
)