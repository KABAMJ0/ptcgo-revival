from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="b515715a-f03d-59c9-ab70-9a4e7ae20569",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTuskex.Name",
    display_name="Great Tusk ex",
    searchable_by=["Great Tusk ex", "Basic", "ex", "Ancient", "GreatTuskex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=53,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Ability(
            title="Quaking Demolition",
            game_text="Once at the end of your turn (after your attack), if this Pok\u00e9mon is in the Active Spot, you must discard the top 5 cards of your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Great Bash",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=260,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)